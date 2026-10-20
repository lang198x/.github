"""Export Lang198x using the family generator's genuine Oxanium glyph geometry."""
from pathlib import Path
from html import escape
import hashlib
import xml.etree.ElementTree as ET
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path

ROOT = Path(__file__).resolve().parent
font_path = ROOT / "fonts/Oxanium[wght].ttf"
if hashlib.sha256(font_path.read_bytes()).hexdigest() != "2ce01d946e1e1ffc8d7eecfffbda8623bedd63eaf811a20488c4b69af45babb0":
    raise ValueError("Oxanium source differs from the family's verified font")
font = instantiateVariableFont(TTFont(font_path), {"wght": 800}, inplace=False)
FONTS = {"prefix": font, "suffix": font}

def pair_adjustments(font,names):
    adjustments=[0]*len(names)
    if 'GPOS' not in font: return adjustments
    # Apply the font's actual kern-feature pair adjustments for these Latin marks.
    features=font['GPOS'].table.FeatureList.FeatureRecord
    indices={i for feature in features if feature.FeatureTag=='kern' for i in feature.Feature.LookupListIndex}
    for i in indices:
        lookup=font['GPOS'].table.LookupList.Lookup[i]
        for raw in lookup.SubTable:
            sub=raw.ExtSubTable if lookup.LookupType==9 else raw
            if not hasattr(sub,'Coverage'): continue
            for at,(left,right) in enumerate(zip(names,names[1:])):
                if left not in sub.Coverage.glyphs: continue
                value=None
                if sub.Format==1:
                    pairset=sub.PairSet[sub.Coverage.glyphs.index(left)]
                    for record in pairset.PairValueRecord:
                        if record.SecondGlyph==right: value=record.Value1; break
                elif sub.Format==2:
                    a=sub.ClassDef1.classDefs.get(left,0); b=sub.ClassDef2.classDefs.get(right,0)
                    value=sub.Class1Record[a].Class2Record[b].Value1
                if value is not None: adjustments[at]+=getattr(value,'XAdvance',0) or 0
    return adjustments

def lettering(text,colour,x=0,y=0,scale=1,role=None):
    role=role or ('suffix' if text in ('198x','8x','x') else 'prefix')
    font=FONTS[role]; glyphs=font.getGlyphSet(); cmap=font.getBestCmap()
    missing=[c for c in text if ord(c) not in cmap]
    if missing: raise ValueError(f'Missing real-font glyphs in {role}: {missing}')
    names=[cmap[ord(c)] for c in text]
    adjustments=pair_adjustments(font,names)
    bounds=BoundsPen(glyphs); pen=SVGPathPen(glyphs); at=0
    for index,name in enumerate(names):
        glyphs[name].draw(TransformPen(pen,(1,0,0,1,at,0)))
        glyphs[name].draw(TransformPen(bounds,(1,0,0,1,at,0)))
        at+=font['hmtx'][name][0]+adjustments[index]
    xmin,ymin,xmax,ymax=bounds.bounds
    factor=72/(ymax-ymin)
    width=(xmax-xmin)*factor
    flattened=SVGPathPen(None)
    matrix=(factor*scale,0,0,-factor*scale,x-xmin*factor*scale,y+ymax*factor*scale)
    parse_path(pen.getCommands(),TransformPen(flattened,matrix))
    return f'<path fill="{colour}" d="{flattened.getCommands()}"/>',width

def svg(title,w,h,content):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title,quote=True)}"><title>{escape(title)}</title>{content}</svg>'


def build():
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    variants = [("colour", "#dbbd00", "#ffcb05"),
                ("light", "#746300", "#171717"),
                ("black", "#171717", "#171717"),
                ("white", "#ffffff", "#ffffff")]
    for name, prefix, suffix in variants:
        left, width = lettering("LANG", prefix)
        right, tail = lettering("198x", suffix, width + 12)
        (assets / f"lang-{name}.svg").write_text(
            svg("Lang198x", width + 12 + tail, 72, left + right) + "\n")
    for name, fill, ink in [("colour", "#dbbd00", "#111111"),
                            ("black", "#171717", "#ffffff"),
                            ("white", "#ffffff", "#171717")]:
        _, width = lettering("L", ink)
        scale = min(36 / width, 36 / 72)
        letter, _ = lettering("L", ink, (64 - width * scale) / 2,
                              (64 - 72 * scale) / 2, scale)
        content = f'<rect width="64" height="64" rx="12" fill="{fill}"/>' + letter
        (assets / f"lang-icon-{name}.svg").write_text(
            svg("Lang198x", 64, 64, content) + "\n")
    for path in assets.glob("*.svg"):
        root = ET.fromstring(path.read_text())
        _, _, width, height = map(float, root.attrib["viewBox"].split())
        bounds = BoundsPen(None)
        for node in root:
            if node.tag.endswith("path"):
                parse_path(node.attrib["d"], bounds)
        x0, y0, x1, y1 = bounds.bounds
        if not (-.001 <= x0 <= x1 <= width + .001 and -.001 <= y0 <= y1 <= height + .001):
            raise ValueError(f"Clipped lettering: {path.name}")
        if "icon" in path.name and (abs((x0+x1)/2-32)>.001 or abs((y0+y1)/2-32)>.001):
            raise ValueError(f"Uncentred initial: {path.name}")
    try:
        lettering("\U0010ffff", "#000000")
    except ValueError:
        pass
    else:
        raise AssertionError("Missing glyph did not fail")
    print("Verified seven SVGs, font hash, bounds, initial centring and missing-glyph rejection.")

if __name__ == "__main__":
    build()
