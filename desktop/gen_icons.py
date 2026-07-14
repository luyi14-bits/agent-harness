"""Generate a proper .ico file from PNG data."""
import struct
import zlib

def create_png(width, height, color=(52, 152, 219)):
    def chunk(chunk_type, data):
        c = chunk_type + data
        crc = struct.pack('>I', zlib.crc32(c) & 0xffffffff)
        return struct.pack('>I', len(data)) + c + crc
    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    raw = b''
    for y in range(height):
        raw += b'\x00'
        for x in range(width):
            raw += bytes(color)
    idat = chunk(b'IDAT', zlib.compress(raw))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

def create_ico(png_data, sizes=[(32, 32), (48, 48), (64, 64), (128, 128)]):
    """Create a proper .ico file with multiple PNG entries."""
    entries = []
    for w, h in sizes:
        data = create_png(w, h)
        entries.append((w, h, data))
    
    header = struct.pack('<HHH', 0, 1, len(entries))
    offset = 6 + 16 * len(entries)
    dir_entries = b''
    for w, h, data in entries:
        bpp = 32
        dir_entries += struct.pack(
            '<BBBBHHIH',
            w if w < 256 else 0,
            h if h < 256 else 0,
            0,  # colors
            0,  # reserved
            1,  # planes
            bpp,
            len(data),
            offset
        )
        offset += len(data)
    result = header + dir_entries
    for _, _, data in entries:
        result += data
    return result

# Generate icons
png_data = create_png(128, 128)
ico_data = create_ico(png_data)

with open('src-tauri/icons/icon.ico', 'wb') as f:
    f.write(ico_data)
with open('src-tauri/icons/icon.png', 'wb') as f:
    f.write(png_data)
with open('src-tauri/icons/128x128.png', 'wb') as f:
    f.write(create_png(128, 128))
with open('src-tauri/icons/128x128@2x.png', 'wb') as f:
    f.write(create_png(256, 256))
with open('src-tauri/icons/32x32.png', 'wb') as f:
    f.write(create_png(32, 32))

import os
for f in ['icon.ico', 'icon.png', '128x128.png', '128x128@2x.png', '32x32.png']:
    path = f'src-tauri/icons/{f}'
    print(f'  {f}: {os.path.getsize(path)} bytes')
print('Icons done')
