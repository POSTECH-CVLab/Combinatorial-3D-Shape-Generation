import os

import constants


STR_PRE = '<?xml version="1.0" encoding="utf-8"?>\n\n<scene version="0.5.0">\n<integrator type="direct"> <integer name="bsdfSamples" value="4"/> <integer name="emitterSamples" value="8"/> <boolean name="hideEmitters" value="true"/> </integrator>\n<emitter type="envmap" id="Area_002-light"> <string name="filename" value="envmap.exr"/> <transform name="toWorld"> <rotate y="1" angle="215"/> <matrix value="1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 "/> </transform> <float name="scale" value="7"/> </emitter>\n<bsdf type="twosided" id="white"> <bsdf type="plastic"> <srgb name="diffuseReflectance" value="0.4 0.4 0.4"/> <string name="intIOR" value="pet"/> <float name="roughness" value="0.01"/> </bsdf> </bsdf>\n<bsdf type="twosided" id="red"> <bsdf type="plastic"> <srgb name="diffuseReflectance" value="0.4, 0.05, 0.05"/> <string name="intIOR" value="pet"/> <float name="roughness" value="0.01"/> </bsdf> </bsdf>\n<bsdf type="twosided" id="green"> <bsdf type="plastic"> <srgb name="diffuseReflectance" value="0.05, 0.4, 0.05"/> <string name="intIOR" value="pet"/> <float name="roughness" value="0.01"/> </bsdf> </bsdf>\n<bsdf type="twosided" id="blue"> <bsdf type="plastic"> <srgb name="diffuseReflectance" value="0.05, 0.05, 0.4"/> <string name="intIOR" value="pet"/> <float name="roughness" value="0.01"/> </bsdf> </bsdf>\n\n'

STR_SHAPE = '<shape type="ply"> <string name="filename" value="{}/{}_{}.ply"/> <ref id="{}"/> </shape>'

STR_POST = '\n<shape type="obj"> <string name="filename" value="plane.obj"/> <transform name="toWorld"> <translate x="0" y=".3" z="0"/> </transform> <bsdf type="diffuse"> <spectrum name="reflectance" value="0.5"/> </bsdf> </shape>\n<sensor type="perspective"> <string name="fovAxis" value="smaller"/> <float name="focusDistance" value="10000"/>\n\n<transform name="toWorld">\n<lookAt origin="0.01, 15.0, 0.0" target="0.0, 0.0, 0.0" up="0.0, 1.0, 0.0"/>\n</transform>\n\n<float name="fov" value="18"/>\n\n<sampler type="ldsampler"> <integer name="sampleCount" value="128"/> </sampler>\n<film type="ldrfilm"> <integer name="width" value="1024"/> <integer name="height" value="768"/> <boolean name="banner" value="false"/> <string name="pixelFormat" value="rgb"/> <rfilter type="gaussian"/> </film>\n</sensor>\n</scene>'

LIST_COLORS = ['red', 'blue', 'green']


def generate(str_path, str_file, num_shapes):
    str_file_ = os.path.join(str_path, str_file + '.xml')

    if not os.path.exists(str_file_):
        print('Generating {}'.format(str_file))
        file_ = open(str_file_, 'w')
        file_.write(STR_PRE)

        for ind_shape in range(1, num_shapes + 1):
            file_.write(STR_SHAPE.format(str_file, str_file, ind_shape, LIST_COLORS[(ind_shape - 1) % len(LIST_COLORS)]))
            file_.write('\n')
    
        file_.write(STR_POST)
        file_.close()
    else:
        print('{} is skipped.'.format(str_file))


if __name__ == '__main__':
    str_files = os.listdir(constants.PATH_MESHES)
    str_files.sort()
    print(str_files)

    for str_file in str_files:
        str_path_file = os.path.join(constants.PATH_MESHES, str_file)
        print(str_path_file)

        if os.path.isdir(str_path_file):
            str_plys = os.listdir(str_path_file)
            if 'single_brick' in str_file:
                num_shapes = 1
            else:
                num_shapes = len(str_plys) - 1
            print(num_shapes)

            generate(constants.PATH_MESHES, str_file, num_shapes)

