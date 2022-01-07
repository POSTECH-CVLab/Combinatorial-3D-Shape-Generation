# Combinatorial-3D-Shape-Generation

This is an official repository of paper "Combinatorial 3D Shape Generation via Sequential Assembly".

* arXiv Preprint: [(abs)](https://arxiv.org/abs/2004.07414), [(pdf)](https://arxiv.org/pdf/2004.07414.pdf)
* [High-Resolution Version](http://jungtaek.github.io/papers/final_ml4eng_2020_high_resolution.pdf) (About 50MB)

## Installing Required Python Packages (Python 3.7)

You are able to install required Python packages by commanding `pip install -r requirements.txt`.

## Running

* Creating a dataset

Run the following script.

```shell
# Move to src_dataset/
$ ./dataset_all.sh 
```

It will create a dataset, which has already been included in the repository.

* Generating a 3D shape

```shell
# Move to src_generation/
$ python assemble_with_bo.py --ind_class 21 --ind_target 1 --use_stability --use_rollback
```

`ind_class` and `ind_target` indicate the indices of class and target object, respectively (Please check the code for dataset creation).
`use_stability` and `use_rollback` are flags for considering stability and using a rollback step.

* Creaing an XML file and its corresponding PLY files

Run the following script.

```shell
# Move to src_rendering/
$ ./meshes_all.sh 
```

It requires a rendering process with [Mitsuba renderer](http://mitsuba-renderer.org/index_old.html).
After changing the camera position and its perspective, render the XML file you want.

## Connection Types Between Two 2-by-4 Bricks

<p align="center">
<img src="./meshes/label01_01.png" width="80" />
<img src="./meshes/label01_02.png" width="80" />
<img src="./meshes/label01_03.png" width="80" />
<img src="./meshes/label01_04.png" width="80" />
<img src="./meshes/label01_05.png" width="80" />
<img src="./meshes/label01_06.png" width="80" />
<img src="./meshes/label01_07.png" width="80" />
<img src="./meshes/label01_08.png" width="80" />
<img src="./meshes/label01_09.png" width="80" />
<img src="./meshes/label01_10.png" width="80" />
<img src="./meshes/label01_11.png" width="80" />
<img src="./meshes/label01_12.png" width="80" />
<img src="./meshes/label01_13.png" width="80" />
<img src="./meshes/label01_14.png" width="80" />
<img src="./meshes/label01_15.png" width="80" />
<img src="./meshes/label01_16.png" width="80" />
<img src="./meshes/label01_17.png" width="80" />
<img src="./meshes/label01_18.png" width="80" />
<img src="./meshes/label01_19.png" width="80" />
<img src="./meshes/label01_20.png" width="80" />
<img src="./meshes/label01_21.png" width="80" />

<img src="./meshes/label02_01.png" width="80" />
<img src="./meshes/label02_02.png" width="80" />
<img src="./meshes/label02_03.png" width="80" />
<img src="./meshes/label02_04.png" width="80" />
<img src="./meshes/label02_05.png" width="80" />
<img src="./meshes/label02_06.png" width="80" />
<img src="./meshes/label02_07.png" width="80" />
<img src="./meshes/label02_08.png" width="80" />
<img src="./meshes/label02_09.png" width="80" />
<img src="./meshes/label02_10.png" width="80" />
<img src="./meshes/label02_11.png" width="80" />
<img src="./meshes/label02_12.png" width="80" />
<img src="./meshes/label02_13.png" width="80" />
<img src="./meshes/label02_14.png" width="80" />
<img src="./meshes/label02_15.png" width="80" />
<img src="./meshes/label02_16.png" width="80" />
<img src="./meshes/label02_17.png" width="80" />
<img src="./meshes/label02_18.png" width="80" />
<img src="./meshes/label02_19.png" width="80" />
<img src="./meshes/label02_20.png" width="80" />
<img src="./meshes/label02_21.png" width="80" />
<img src="./meshes/label02_22.png" width="80" />
<img src="./meshes/label02_23.png" width="80" />
<img src="./meshes/label02_24.png" width="80" />
<img src="./meshes/label02_25.png" width="80" />
</p>

## Examples in Combinatorial 3D Shape Dataset

* Bar
<p align="center">
<img src="./meshes/label11_22.png" width="180" />
<img src="./meshes/label11_25.png" width="180" />
<img src="./meshes/label11_28.png" width="180" />
</p>

* Line
<p align="center">
<img src="./meshes/label12_19.png" width="180" />
<img src="./meshes/label12_21.png" width="180" />
<img src="./meshes/label12_23.png" width="180" />
</p>

* Plate
<p align="center">
<img src="./meshes/label13_20.png" width="180" />
<img src="./meshes/label13_22.png" width="180" />
<img src="./meshes/label13_24.png" width="180" />
</p>

* Wall
<p align="center">
<img src="./meshes/label14_13.png" width="180" />
<img src="./meshes/label14_18.png" width="180" />
<img src="./meshes/label14_23.png" width="180" />
</p>

* Cuboid
<p align="center">
<img src="./meshes/label15_20.png" width="180" />
<img src="./meshes/label15_27.png" width="180" />
<img src="./meshes/label15_30.png" width="180" />
</p>

* Square Pyramid
<p align="center">
<img src="./meshes/label16_03.png" width="180" />
<img src="./meshes/label16_04.png" width="180" />
<img src="./meshes/label16_05.png" width="180" />
</p>

* Chair
<p align="center">
<img src="./meshes/label21_03.png" width="180" />
<img src="./meshes/label21_07.png" width="180" />
<img src="./meshes/label21_12.png" width="180" />
</p>

* Sofa
<p align="center">
<img src="./meshes/label22_09.png" width="180" />
<img src="./meshes/label22_21.png" width="180" />
<img src="./meshes/label22_28.png" width="180" />
</p>

* Cup
<p align="center">
<img src="./meshes/label23_05.png" width="180" />
<img src="./meshes/label23_07.png" width="180" />
<img src="./meshes/label23_18.png" width="180" />
</p>

* Hollow
<p align="center">
<img src="./meshes/label24_08.png" width="180" />
<img src="./meshes/label24_10.png" width="180" />
<img src="./meshes/label24_24.png" width="180" />
</p>

* Table
<p align="center">
<img src="./meshes/label25_07.png" width="180" />
<img src="./meshes/label25_12.png" width="180" />
<img src="./meshes/label25_15.png" width="180" />
</p>

* Car
<p align="center">
<img src="./meshes/label26_03.png" width="180" />
<img src="./meshes/label26_12.png" width="180" />
<img src="./meshes/label26_18.png" width="180" />
</p>

## Citation
```
@article{KimJ2020arxiv,
    author={Kim, Jungtaek and Chung, Hyunsoo and Lee, Jinhwi and Cho, Minsu and Park, Jaesik},
    title={Combinatorial {3D} Shape Generation via Sequential Assembly},
    journal={{arXiv} preprint {arXiv}:2004.07414},
    year={2020}
}
```

or

```
@inproceedings{KimJ2020neuripsw,
    author={Kim, Jungtaek and Chung, Hyunsoo and Lee, Jinhwi and Cho, Minsu and Park, Jaesik},
    title={Combinatorial {3D} Shape Generation via Sequential Assembly},
    booktitle={NeurIPS Workshop on Machine Learning for Engineering Modeling, Simulation, and Design (ML4Eng)},
    year={2020}
}
```

## Contributor
* Jungtaek Kim: [jtkim@postech.ac.kr](mailto:jtkim@postech.ac.kr)
* Hyunsoo Chung: [hschung2@postech.ac.kr](mailto:hschung2@postech.ac.kr)

## License
[MIT License](LICENSE)
