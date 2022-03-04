import zipfile
from xml.dom import minidom


def kmz_to_kml(file_kmz_kmz):
    """save kmz to kml"""
    zf = zipfile.ZipFile(file_kmz, 'r')
    for fn in zf.namelist():
        if fn.endswith('.kml'):
            content = zf.read(fn)
            xmldoc = minidom.parseString(content)
            out_name = (file_kmz.replace(".kmz", ".kml")).replace("\\", "/")
            with open(out_name, 'w') as out:
                out.writelines(xmldoc.toxml())
        else:
            print("no kml file_kmz")


if __name__ == "__main__":
    file_kmz = r"/home/victor/Documents/Projects/Pessoal/kmz-to-kml/test.kmz"
    kmz_to_kml(file_kmz)
