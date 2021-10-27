

from app.data import FileDataProvider


for res in FileDataProvider('./test/sample_data.dat').read():
    print(res)