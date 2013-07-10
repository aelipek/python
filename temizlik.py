cumle=input("cümle giriniz")
derle = re.compile(",|\.|\'|:|;|\"|\*|-|_|\?|!|\^|\&|\)|=|\(",re.IGNORECASE|re.UNICODE)
cumle=derle.sub("",cumle)
