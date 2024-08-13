import subprocess
import os

minyak = [
    ['rm', '-rf', '~/tmp/*', '~/tmp', '~/asd/models/Stable-diffusion/tmp_models', '~/asd/models/Lora/tmp_Lora', '~/asd/models/unet/tmp_unet'],
    ['mkdir', '-p', '~/asd/models/Lora'],
    ['mkdir', '-p', '~/asd/models/ESRGAN'],
    ['mkdir', '-p', '~/asd/models/unet'],
    ['ln', '-vs', '/tmp', '~/tmp'],
    ['ln', '-vs', '/tmp/models', '~/asd/models/Stable-diffusion/tmp_models'],
    ['ln', '-vs', '/tmp/unet', '~/asd/models/Lora/tmp_unet'],
    ['ln', '-vs', '/tmp/Lora', '~/asd/models/Lora/tmp_Lora'],
]

for tepung in minyak:
    gorengan = [os.path.expanduser(arg) for arg in tepung]
    subprocess.run(gorengan, check=True)