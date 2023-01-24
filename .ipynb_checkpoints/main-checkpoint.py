{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "07a74b10",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "dc2705b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#File path\n",
    "school_data_to_combine = \"Resources/schools_complete.csv\"\n",
    "student_data_to_combine = \"Resources/students_complete.csv\"\n",
    "\n",
    "# Read School and Student Data File and store into Pandas DataFrames\n",
    "school_data = pd.read_csv(school_data_to_combine)\n",
    "student_data = pd.read_csv(student_data_to_combine)\n",
    "\n",
    "\n",
    "# Combine the data into a single dataset.  \n",
    "school_data_total = pd.merge(student_data, school_data, how=\"left\", on=[\"school_name\", \"school_name\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "0d2ccc2d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#total number of uniques schools\n",
    "school_total_unique = school_data['school_name'].unique()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "732c542d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(school_total_unique)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08b53212",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2b030896",
   "metadata": {},
   "outputs": [],
   "source": [
    "#total number of students\n",
    "total_students = school_data_total['student_name'].count()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e1ea011",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2db7fb59",
   "metadata": {},
   "outputs": [],
   "source": [
    "#calculate total budget for schools\n",
    "total_budget = school_data['budget'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "11c5b9c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculate avg math score round up????????\n",
    "average_math_score = school_data_total['math_score'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4c258b56",
   "metadata": {},
   "outputs": [],
   "source": [
    "#calculate avg reading score roundup????\n",
    "average_reading_score = school_data_total['reading_score'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f7b2f8ee",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'>=' not supported between instances of 'set' and 'int'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/sr/pdhryvkj29v9v3m0rlsrr8dm0000gn/T/ipykernel_3744/668981628.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#percentage passing math\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mtotal_pass_math\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mschool_data_total\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m'math_score'\u001b[0m\u001b[0;34m}\u001b[0m \u001b[0;34m>=\u001b[0m\u001b[0;36m70\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mavg_pass_math\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtotal_pass_math\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtotal_number_students\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m1000\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: '>=' not supported between instances of 'set' and 'int'"
     ]
    }
   ],
   "source": [
    "#percentage passing math\n",
    "total_pass_math = school_data_total.loc[{'math_score'} >=70]\n",
    "avg_pass_math = len(total_pass_math)/([total_number_students] * 1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b9369397",
   "metadata": {},
   "outputs": [],
   "source": [
    "#percentage passing reading\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "2488a07e",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'math_score'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key, method, tolerance)\u001b[0m\n\u001b[1;32m   2645\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2646\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2647\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'math_score'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/sr/pdhryvkj29v9v3m0rlsrr8dm0000gn/T/ipykernel_3744/3491499817.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m school_data.loc[(school_data['math_score'] > 70) &\\\n\u001b[0m\u001b[1;32m      2\u001b[0m (school_data['math_score'] < 69)]\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   2798\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnlevels\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2799\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_getitem_multilevel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2800\u001b[0;31m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2801\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2802\u001b[0m                 \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key, method, tolerance)\u001b[0m\n\u001b[1;32m   2646\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2647\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2648\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_maybe_cast_indexer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2649\u001b[0m         \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_indexer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtolerance\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtolerance\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2650\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mindexer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mndim\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mindexer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msize\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'math_score'"
     ]
    }
   ],
   "source": [
    " school_data.loc[(school_data['math_score'] > 70) &\\\n",
    " (school_data['math_score'] < 69)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "670538e5",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mFailed to start the Kernel. \n",
      "\u001b[1;31mKernel Python 3.9.6 is not usable. Check the Jupyter output tab for more information. \n",
      "\u001b[1;31mView Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c9eadc7",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mFailed to start the Kernel. \n",
      "\u001b[1;31mKernel Python 3.9.6 is not usable. Check the Jupyter output tab for more information. \n",
      "\u001b[1;31mView Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "508bf1ac",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mFailed to start the Kernel. \n",
      "\u001b[1;31mKernel Python 3.9.6 is not usable. Check the Jupyter output tab for more information. \n",
      "\u001b[1;31mView Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details."
     ]
    }
   ],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  },
  "vscode": {
   "interpreter": {
    "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
