try:
    with(
    open("ADVANCED PYTHON/file1.txt") as f1,
    open("ADVANCED PYTHON/file2.txt") as f2
    ):
      print("file opened successfull")
except FileNotFoundError:
   print("file not found!!!!!!!! please create one🙌")