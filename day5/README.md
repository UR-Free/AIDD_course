# AIDD_course
Day 5 course


## ColabFold
```
conda create -n colab python=3.10
conda activate colab
pip install -U "jax[cuda12]"
pip install "colabfold[alphafold-minus-jax]"
pip install --upgrade tensorflow
pip install silence_tensorflow
git clone git@github.com:sokrypton/ColabFold.git
cd ColabFold
# pip install . seems not work for me, change to below
pip install . --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install "colabfold[alphafold]"
```

## DiffDock
see https://github.com/UR-Free/DiffDock

## SurfDock
see https://github.com/UR-Free/SurfDock

## DrugClip
see https://github.com/UR-Free/DrugCLIP
