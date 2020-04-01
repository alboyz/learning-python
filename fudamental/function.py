def totalHarga(beli, hargaBaju=10000):
    total = hargaBaju*beli
    print("anda membeli", beli, "baju", "harganya",
          hargaBaju, "jadi totalnya adalah:", total)
    return total


transaksi = totalHarga(2)
