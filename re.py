# -*- coding: utf-8 -*-
"""RE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aShDY7sJlcEzYUGqZYSvUbw-WF-LHAnT
"""

! pip install deeppavlov

!python -m deeppavlov download re_docred

!pip install transformers

import numpy as np
import transformers
from transformers import BertTokenizer
from deeppavlov.core.commands.utils import expand_path
from deeppavlov import configs, build_model
model = build_model(configs.relation_extraction.re_docred, download=False)

sentence_tokens = [["Barack", "Obama", "is", "married", "to", "Michelle", "Obama", ",", "born", "Michelle", "Robinson", "."]]
entity_pos = [[[(0, 2)], [(5, 7), (9, 11)]]]
entity_tags = [["PER", "PER"]]
pred = model(sentence_tokens, entity_pos, entity_tags)

print(pred)

#python -m deeppavlov train re_docred