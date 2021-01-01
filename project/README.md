## ELMED219-2021 (team-based project)

(MittUiB: [ELMED219 21V](https://mitt.uib.no/courses/27607))

# _Precision medicine and quantitative imaging in glioblastoma_



## Description
Imagine that you are a group of established successful scientists that will team up to tackle an important biomedical and medical challenge. There is an open call for research proposals under a new umbrella program entitled “Artificial intelligence and computational (bio)medicine”, where your multidisciplinary group are aiming for a project on “Precision medicine and quantitative imaging in glioblastoma - a multiscale approach”.

The focus of the assignment is **(i)** description of relevant imaging technologies and modalities - possibly at different scales, **(ii)** proposal of imaging-derived biomarkers for glioblastoma, **(iii)** machine learning techniques for segmentation, classification, treatment stratification and prediction, **(iv)** the novelty and expected impact of your approach, and **(v)** the evaluation of the ethics of your project together with a data management plan (and not so much the basic science of brain tumors per se).


## Organization of your report

### Research plan
(3-5 pages incl. figures and bibliography)
 - A brief background to the field
 - Objectives and expected impact
 - Material and methods
 - Evaluation

### Data management plan and ethical considerations
(1 1/2-2 1/2 pages incl. graphics / links)
 - Description of generated data and code
 - Sharing of data and code
 - Ethical considerations

-----------------------------------
## *Prepare you and your computer for the team-based project*



#### *Orient yourself in the material for the group project and how to use [LaTeX](https://www.latex-project.org) for writing your report*
<!-- _Note: Details will be modified and added before the course start_ -->

- We will be using the [Overleaf](https://www.overleaf.com) online, collaborative LaTeX editor (for more information on LaTeX, see [here](https://en.wikipedia.org/wiki/LaTeX) and [here](https://www.tug.org/pracjourn/2007-4/senthil/senthil.pdf) and [here](https://mildopinions.wordpress.com/2008/07/07/why-i-use-latex-in-biology), and for LeTeX templates, see e.g. [here](https://www.overleaf.com/latex/templates/template-for-submissions-to-molecular-systems-biology/kyxgttpbzhht) and [here](https://www.overleaf.com/latex/templates/tagged/academic-journal))

- **LaTeX template for the report**  is found [[here](./latex-template/ELMED219_2021_project_team_k.tex)] with a dummy figure [[here](./latex-template/elmed219_dummy_fig.png)], resulting in the following [[pdf](./latex-template/ELMED219_2021_project_team_k.pdf)].

- **Expected level of detail** is illustrated with a [project report](https://www.overleaf.com/read/xwjxwcnpzhqv) from the 2019 Summer School at Seili (for which *Prostate Cancer* was the topic) to be found on Overleaf [[here](https://www.overleaf.com/project/5ec71af71aca320001385354)] and on the present repo as [[main.tex](./latex-template/main.tex)],  [[fig1](./latex-template/Fig1_The_process_of_autoEncoder.png)], [[fig2](./latex-template/Fig2_Overview_of_the_process.png)], resulting in the [[pdf](./latex-template/Seili_2020_project_template.pdf)].



### Some sources of information  (brain tumors - neuroimaging - AI - software & data)<br>


#### Pre reading

  - For those of you that have limited knowledge about biology and pathology of brain or want to refresh their knowledge, we recommend the free Coursera course
  https://www.coursera.org/learn/neurobiology, especially the lecture on [brain tumors](https://www.coursera.org/lecture/neurobiology/brain-tumors-fUcn4).
  - Aldape K et al. Challenges to curing primary brain tumors. Nat Rev Clin Oncol 2019;16:509-520.  [[link](https://www.nature.com/articles/s41571-019-0177-5)]

  - Louis DN et al. The 2016 World Health Organization Classification of Tumors of the Central Nervous System: A Summary. Acta Neuropathol 2016;131(6):803-820. [[link](https://link.springer.com/article/10.1007/s00401-016-1545-1)]

  - The Brain Atlas https://www.proteinatlas.org/humanproteome/brain


**Brain tumors & Neuroimaging** (some pointers)

- Abd-Ellah MK et al. A review on brain tumor diagnosis from MRI images: Practical implications, key achievements, and lessons learned. Magnetic Resonance Imaging 2019;61:300-318. [[link](https://www.sciencedirect.com/science/article/pii/S0730725X18304302)]
- Hamid MAA, Khan NA. Investigation and Classification of MRI Brain Tumors Using Feature Extraction Technique. Journal of Medical and Biological Engineering 2020;40:307–317. [[link](https://link.springer.com/article/10.1007/s40846-020-00510-1)]
- Lohmann P et al. PET/MRI Radiomics in Patients With Brain Metastases. Front. Neurol., 07 February 2020. [[link](https://www.frontiersin.org/articles/10.3389/fneur.2020.00001/full)]
- Tiwari A et al. Brain tumor segmentation and classification from magnetic resonance images: Review of selected methods from 2014 to 2019. Pattern Recognition Letters 2020;131:244-260. [[link](https://www.sciencedirect.com/science/article/pii/S016786551930340X)]
- Nadeem MW et al. Brain Tumor Analysis Empowered with Deep Learning: A Review, Taxonomy, and Future Challenges. Brain Sci 2020;10(2):118. [[link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7071415)]

- Brain Tumor Segmentation (BraTS) Challenge 2020: Scope  (MICCAI2020) - Center for Biomedical Image Computing & Analytics, Perelman School of Medicine, University of Pennsylvania [[link](https://www.med.upenn.edu/cbica/brats2020)] [[Data description](https://www.med.upenn.edu/cbica/brats2020/data.html)]


**Brain tumors & Artificial intelligence** (some pointers)

- NCI: Artificial Intelligence Expedites Brain Tumor Diagnosis during Surgery. 2020 Feb 12. [[link](https://www.cancer.gov/news-events/cancer-currents-blog/2020/artificial-intelligence-brain-tumor-diagnosis-surgery#:~:text=Now%2C%20a%20new%20study%20shows,tumor%20tissue%20from%20healthy%20tissue)]
- Hollon TC et al. Near Real-Time Intraoperative Brain Tumor Diagnosis Using Stimulated Raman Histology and Deep Neural Networks. Nature Medicine 2020;26(1):52-58. [[link](https://www.nature.com/articles/s41591-019-0715-9)]  [[GitHub repository](https://github.com/toddhollon/srh_cnn)] [[video](https://labblog.uofmhealth.org/health-tech/artificial-intelligence-improves-brain-tumor-diagnosis?utm_source=youtube&utm_medium=organic&utm_campaign=ai_neuro&utm_content=labblog)]
- Yogananda CGB et al. A novel fully automated MRI-based deep-learning method for classification of IDH mutation status in brain gliomas. Neuro-Oncology 2020;22(3):402–411. [[link](https://watermark.silverchair.com/noz199.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAsQwggLABgkqhkiG9w0BBwagggKxMIICrQIBADCCAqYGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM_l0qCe0X3j7sec-zAgEQgIICd-ksYewnKy45LqXTHXhHOAzzJHK3d4tFLFHnfz8trcRb48Op3XkTRQnJTc68VoXcq-91GkhszdO1gk8fttfzAwFwW5XMt_eLL4rqoKEbl2mNWd3wzyvmluUTIWhhmnLFvEWPTHh6PW1CpBxGu_T3RwFvulqSVi-DWv_K37kCY4DY-5nROmyiX6ZI0G77UhPodnbG0S8LjAz02cK0xfz2fpahloSHSm8TfTzWz_AlUKLJEKmdNMVQuy9x7uhAHVYQwf_sS6Q2gAz09ETmmfO3DzwPA34F_ss3vszaphRudvW1aMteB9K6eqWYmqOiMfI4r8LFM_fzoLzLk9JvtQJv8KjJXkOorVG7oVFh-jiIrOnQgV1IJ0xKYLv1maRksi6J4SmpO0gDY5XXVH8Vih99007mvG_nr-E7UtFz5dUUyzERxW6O_1dvClEjpokBpDP-JBxyOwibwNQobzV8c4sT7n99wIVWOgwwJNEKADqHYECBuEH2wO0NT0_pBlJx0JAJQL8i-dg949euJo_gKqq8DHOymDDkaEd4o-QXgsJ5bMZiZ3iiH-xUAlJsdh2UxLLGCEKezghbLN40_qf_yVhH-NLM_8JbTI-nVuxH2a-dIaHAu0Q_YmHpItMRzBYxNrud99epxTorOe1RgKGhr2Hp8Xb7EGYvJNDC-4ymCTWlB2pET8NudI1e7YZBRH9UDmc6GYJbZnryuYbpWUvR5_rm7FicF8-gysEn9cIVW6vycxsLPompsjQhXrkLJWYOCLBt1P1_blJVk8ASUpzOTPNjhngR4ZfGdgs8_aRF-15kzdsqDA2Id1QqMwZsXRL8PtydJWMP3HXkM3k)]
- Kickinereer P et al. Automated quantitative tumour response assessment of MRI in neuro-oncology with artificial neural networks: a multicentre, retrospective study. The Lancet Oncology 2019;20(5):728-740. [[link](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30098-1/fulltext)]

**Brain tumors & software and data** (some pointers for illustration and inspiration)

- Brain Tumor Segmentation | Papers With Code [https://paperswithcode.com/task/brain-tumor-segmentation/latest]
- Akshay Kumaar M. Brain Tumor Classification (using ResNet50 and Google Colab)  [https://github.com/aksh-ai/brain_tumor_classification]
- Joohyun Lee. BraTs (Brain Tumor Segmentation) [https://github.com/cv-lee/BraTs]
- Bakas S et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. Scientific Data 2017;4, Article number: 170117 [https://www.nature.com/articles/sdata2017117] [[pdf](https://www.nature.com/articles/sdata2017117.pdf)]<br>
*Excerpt*: Considering the value of big data and the potential of publicly available datasets for increased reproducibility of scientific findings, the National Cancer Institute (NCI) of the National Institutes of Health (NIH) created TCGA ([cancergenome.nih.gov](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga)) and [TCIA](https://link.springer.com/article/10.1007/s10278-013-9622-7) (www.cancerimagingarchive.net). TCGA is a multi-institutional comprehensive collection of various molecularly characterized tumor types, and its data are available in NCI’s Genomic Data Commons portal ([gdc-portal.nci.nih.gov](https://portal.gdc.cancer.gov)). Building upon NIH’s investment in TCGA, the NCI’s Cancer Imaging Program approached sites that contributed tissue samples, to obtain corresponding de-identified routine clinically-acquired radiological data and store them in TCIA. These repositories make available multi-institutional, high-dimensional, multi-parametric data of cancer patients, allowing for radiogenomic analysis.
- Beers A et al. DeepNeuro: an open-source deep learning toolbox for neuroimaging. Neuroinformatics 2020, June 23 [[link]( https://link.springer.com/article/10.1007/s12021-020-09477-5)] [[pdf](https://link.springer.com/content/pdf/10.1007/s12021-020-09477-5.pdf)]; GitHub: https://github.com/QTIM-Lab/DeepNeuro - A deep learning python package for neuroimaging data. Focused on validated command-line tools you can use today. Created by the Quantitative Tumor Imaging Lab at the Martinos Center (Harvard-MIT Program in Health, Sciences, and Technology / Massachusetts General Hospital).
- Chang K et al. Automatic assessment of glioma burden: A deep learning algorithm for fully automated volumetric and bi-dimensional measurement. Neuro-Oncology 2019;21(11):1412-1422 [[link](https://academic.oup.com/neuro-oncology/article/21/11/1412/5514498)] [[pdf](https://scholar.google.com/scholar_url?url=https://academic.oup.com/neuro-oncology/article-pdf/21/11/1412/30391573/noz106.pdf&hl=en&sa=T&oi=ucasa&ct=ufr&ei=de7jX5XYM4-Ny9YPjJ6xwAs&scisig=AAGBfm2TQE4zFdIsfPkZZOKNbcylAzCecA)]. Code: https://github.com/QTIM-Lab/DeepNeuro.
- Ellis DG, Aizenberg MR. Deep Learning Using Augmentation via Registration: 1st Place Solution to the AutoImplant 2020 Challenge. In: Li J., Egger J. (eds) Towards the Automatization of Cranial Implant Design in Cranioplasty. AutoImplant 2020. Lecture Notes in Computer Science, vol 12439. Springer, Cham. [[link](https://link.springer.com/chapter/10.1007%2F978-3-030-64327-0_6)]; Code: https://github.com/ellisdg/3DUnetCNN; Pretrained models: https://zenodo.org/record/4289225; Augmented Data Set: https://zenodo.org/record/4270278
- Ellis DG, Aizenberg MR. Structural brain imaging predicts individual-level task activation maps using deep learning. bioRxiv, 2020 [[link](https://www.biorxiv.org/content/10.1101/2020.10.05.306951v1)] [[pdf](https://www.biorxiv.org/content/10.1101/2020.10.05.306951v1.full.pdf)]; Code: https://github.com/ellisdg/3DUnetCNN;   "... _The reliable functional activation predictions from structural imaging may be of use to clinicians in cases where task activation mapping is critical for patient care, including neurosurgical operative planning. Task mapping predictions could give neurosurgeons the ability to visualize eloquent areas and avoid potential surgically induced deficits, even without collecting any fMRI data. Our future efforts will focus on using CNNs to provide enhanced mapping accuracy and validating the use of structural imaging to predict task activation maps in clinical populations, such as brain tumor patients._"
- Lundervold AS, Lundervold A. An overview of deep learning in medical imaging focusing on MRI. Zeitschrift fur Medizinische Physik. 2019;29(2):102-127. [[link](https://www.sciencedirect.com/science/article/pii/S0939388918301181)] [[pdf](https://reader.elsevier.com/reader/sd/pii/S0939388918301181?token=F0F5572A8CA576BB20A27E381932486EAD2ECEAA5FEE098EAE183438F8BA7A989E8046160DDE10526E3698BD6D27784A)]


David G. Ellis [BraTS 2020 Tutorial](https://github.com/ellisdg/3DUnetCNN/tree/master/examples/brats2020) using [3DUNetCNN](https://github.com/ellisdg/3DUnetCNN):<br>

![Brain Tumor Segmentation (BraTS) Tutorial](https://github.com/ellisdg/3DUnetCNN/raw/master/legacy/doc/tumor_segmentation_illusatration.gif)

### Ethics of artificial intelligence and machine learning (some pointers)
- Wikipedia [https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence]
- Rigby MJ. Ethical Dimensions of Using Artificial Intelligence in Health Care. AMA Journal of Ethics, Feb 2019 [https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02]
- Morley J, Machado C, Burr C et al. The Debate on the Ethics of AI in Health Care: A Reconstruction and Critical Review (November 13, 2019). [https://ssrn.com/abstract=3486518]
- Bostrom N, Yudkowsky E. The Ethics of Artificial Intelligence. In Frankish K, Ramsey W (ed) Cambridge Handbook of Artificial Intelligence, CUP 2014   [https://intelligence.org/files/EthicsofAI.pdf]
- Ethics of Artificial Intelligence and Robotics. First published Apr 30, 2020. Stanford Encyclopedia of Philosophy [https://plato.stanford.edu/entries/ethics-ai]
- Gibney W. The battle for ethical AI at the world’s biggest machine-learning conference. Nature news 20 Jan 2020 [https://www.nature.com/articles/d41586-020-00160-y]
- Ethics of AI in Radiology. European and North America Multisociety Statement 2019 [https://www.acr.org/-/media/ACR/Files/Informatics/Ethics-of-AI-in-Radiology-European-and-North-American-Multisociety-Statement--6-13-2019.pdf]
- Vollmer S, Mateen BA, Bohner G et al. Machine learning and artificial intelligence research for patient benefit: 20 critical questions on transparency, replicability, ethics, and effectiveness. BMJ 2020;368:l6927. [https://www.bmj.com/content/368/bmj.l6927]


__________________________________________________________________________
