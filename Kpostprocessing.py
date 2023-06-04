import SimpleITK as sitk

# 加载原始图像和参考图像
input_image = sitk.ReadImage('Data/Segment_Anything/Study_06_erector_spinae_rightSAM.nii.gz')
ref_image = sitk.ReadImage('Data/Study/msk/Study_06_erector_spinae_right.nii.gz')

# 获取参考图像的空间信息和spacing
ref_origin = ref_image.GetOrigin()
ref_spacing = ref_image.GetSpacing()
ref_direction = ref_image.GetDirection()

input_image.SetOrigin(ref_origin)
input_image.SetSpacing(ref_spacing)
input_image.SetDirection(ref_direction)

# 将结果保存为新的NIfTI文件
sitk.WriteImage(input_image, 'Data/Segment_Anything/Study_06_erector_spinae_right.nii.gz')