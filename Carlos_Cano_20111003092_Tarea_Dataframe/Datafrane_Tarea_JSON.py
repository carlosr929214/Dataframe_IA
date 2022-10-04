{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "d3c248e7-3197-48e2-9b97-d0680b53bf31",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gender</th>\n",
       "      <th>country</th>\n",
       "      <th>career_x</th>\n",
       "      <th>age</th>\n",
       "      <th>career_y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Male</td>\n",
       "      <td>Honduras</td>\n",
       "      <td>Director of Sales</td>\n",
       "      <td>25</td>\n",
       "      <td>Director of Sales</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Female</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>Actuary</td>\n",
       "      <td>41</td>\n",
       "      <td>Actuary</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender   country           career_x age           career_y\n",
       "0    Male  Honduras  Director of Sales  25  Director of Sales\n",
       "1  Female    Mexico            Actuary  41            Actuary"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "path = 'C:..\\\\Carlos_Cano_20111003092_Tarea_Dataframe\\\\'\n",
    "\n",
    "file = 'DATA.json'\n",
    "\n",
    "df = pd.read_json(path + file)\n",
    "\n",
    "df = pd.DataFrame ({\"gender\": [\"Male\",\"Female\"],\n",
    "                   \"country\": [\"Honduras\",\"Mexico\"],\n",
    "                    \"career\": [\"Director of Sales\",\"Actuary\"]})\n",
    "\n",
    "df1 = pd.DataFrame ({\"gender\": [\"Male\",\"Female\"],\n",
    "                   \"age\": [\"25\",\"41\"],\n",
    "                    \"career\": [\"Director of Sales\",\"Actuary\"]})\n",
    "\n",
    "pd.merge(df, df1, on = \"gender\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "606e5fd2-dad7-4b60-b049-eaa6d4fb1f63",
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
