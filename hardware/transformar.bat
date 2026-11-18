for /R %%f in (*.pptx) do (
  python -m pptx2md "%%f" -o "%%f".md
)