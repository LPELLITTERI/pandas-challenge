{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1ce98894",
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
   "id": "0c5e414a",
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
   "id": "b966a133",
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
   "id": "e58d1825",
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
   "id": "65f2ad57",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "11f0762d",
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
   "id": "2a2ee90f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "184abfe7",
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
   "id": "3a304391",
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
   "id": "b39c7495",
   "metadata": {},
   "outputs": [],
   "source": [
    "#calculate avg reading score roundup????\n",
    "average_reading_score = school_data_total['reading_score'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "81aae8c0",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'>' not supported between instances of 'str' and 'int'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/sr/pdhryvkj29v9v3m0rlsrr8dm0000gn/T/ipykernel_3744/3914896018.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m#percentage passing math\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mtotal_pass_math\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mschool_data_total\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'math_score'\u001b[0m \u001b[0;34m>\u001b[0m\u001b[0;36m70\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mavg_pass_math\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtotal_pass_math\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtotal_number_students\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m1000\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: '>' not supported between instances of 'str' and 'int'"
     ]
    }
   ],
   "source": [
    "#percentage passing math\n",
    "total_pass_math = school_data_total.loc['math_score' >70]\n",
    "avg_pass_math = len(total_pass_math)/([total_number_students] * 1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "abc8c9e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#percentage passing reading\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "33c10c7a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (522041184.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/sr/pdhryvkj29v9v3m0rlsrr8dm0000gn/T/ipykernel_3744/522041184.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    school_data.loc[(school_data['math_score'] > 70) & /\u001b[0m\n\u001b[0m                                                       ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    " school_data.loc[(school_data['math_score'] > 70) & /\n",
    " (school_data['math_score'] < 69)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdaf3f76",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e92c171",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cda40c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df926d86",
   "metadata": {},
   "outputs": [],
   "source": []
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
