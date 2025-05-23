# AIDD_course
Day 4 course

```bash
# 首先更新RFdiffusion和dl_binder_design文件夹
cd RFdiffusion
git pull
cd dl_binder_design
git pull
```

## TNFR binder design
```bash
# TNFR binder design
cd RFdiffusion/examples
# free diffusion of 120 residues binder to TNFR
conda activate SE3nv
./design_ppi_TNFR_extended.sh
# ProteinMPNN-Fastrelax
conda activate proteinmpnn_binder_design
cp design_tnfr_extended_*.pdb dl_binder_design/examples/tnfr_designs
cd dl_binder_design/examples
./run_proteinmpnn_relax_tnfr.sh
# AF2 initial guess prediction
conda activate af2_sub
./run_af2_guess_tnfr.sh
# select cases with small pae_interaction, and then go to RFdiffusion dir
conda activate SE3nv
cp design_tnfr_extended_2_dldesign_3_af2pred.pdb RFdiffusion/examples/input_pdbs/
./design_partialdiffusion_tnfr.sh
# ProteinMPNN-Fastrelax
# AF2 initial guess prediction cycle
```

## MSA subsampling for transporter
see https://github.com/PKUfjh/af2_conformations

## MSA clustering for KaiB
see https://github.com/PKUfjh/AF_Cluster
