import subprocess
import os
import shutil

PDF_FILE = "source.pdf"
OUTPUT_DIR = "icons"
INKSCAPE = shutil.which("inkscape")

if INKSCAPE is None:
    print("Inkscape не найден")
    exit()

os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGE_WIDTH = 2560
PAGE_HEIGHT = 1440

COLUMNS = 7
ROWS = 3

icon_width = PAGE_WIDTH / COLUMNS
icon_height = PAGE_HEIGHT / ROWS

MAX_PAGES = 200
icon_index = 1

for page in range(1, MAX_PAGES + 1):

    test = subprocess.run([
        INKSCAPE,
        PDF_FILE,
        f"--pdf-page={page}",
        "--export-type=svg",
        "--export-filename=temp_test.svg"
    ], capture_output=True)

    if test.returncode != 0:
        break

    for row in range(ROWS):
        for col in range(COLUMNS):

            x0 = col * icon_width
            y0 = row * icon_height
            x1 = x0 + icon_width
            y1 = y0 + icon_height

            output_file = os.path.join(
                OUTPUT_DIR,
                f"icon_{icon_index}.svg"
            )

            subprocess.run([
                INKSCAPE,
                PDF_FILE,
                f"--pdf-page={page}",
                f"--export-area={x0}:{y0}:{x1}:{y1}",
                "--export-type=svg",
                f"--export-filename={output_file}"
            ])

            icon_index += 1

print(f"Готово! Экспортировано {icon_index-1} иконок.")
