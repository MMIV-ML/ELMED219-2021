
aff0 = img0_ap.affine
aff0_new = aff0.copy()
aff0_new[2][1]=-1  # Change sign
img0_is = nib.Nifti1Pair(images[0].get_fdata(), aff1_new)
plotting.plot_anat(img0_is, title="flash_060 (IS)")
plotting.show()
