k=0
ima = image.index_img(img, k)
plotting.plot_anat(ima, title=chn_names[k])
ima = image.index_img(img, k+1)
plotting.plot_anat(ima, title=chn_names[k+1])
plotting.show()
