{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<product(珍珠奶茶,60)>, <product(珍珠奶茶,60)>, <product(珍珠奶茶,60)>, <product(珍珠奶茶,60)>, <product(珍珠奶茶,60)>]\n"
     ]
    }
   ],
   "source": [
    "class products:\n",
    "    def __init__(self,name,price):\n",
    "        self.name=name\n",
    "        self.price=price\n",
    "    def __str__(self):\n",
    "        #return self.name+' '+str(self.price)\n",
    "        return f'{self.name} $ {self.price}'\n",
    "    def __repr__(self):\n",
    "        return f'<product({self.name},{self.price})>'\n",
    "    ####相加定義屬性\n",
    "    def __add__(self,other): \n",
    "        if isinstance(other,str):\n",
    "            self.name+=other\n",
    "        if isinstance(other,products):\n",
    "            return [self,other]\n",
    "    ####相乘定義屬性   \n",
    "    def __mul__(self,other):\n",
    "        if isinstance(other,int):\n",
    "            re=[]\n",
    "            for i in range(other):re.append(self)\n",
    "            return re      \n",
    "p1=products('珍珠奶茶',60)\n",
    "p2=products('錫蘭紅茶',30)\n",
    "#p1+p2\n",
    "#p+'紅玉'\n",
    "print(p1*5)\n",
    "#print(repr(p))  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
