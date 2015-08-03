# coding: utf8
# OeQ autogenerated lookup function for 'U-Values of Roofs as Projection (method 2) in correlation to year of construction, based on the source data of the survey for the "German Building Typology developed by the "Institut für Wohnen und Umwelt", Darmstadt/Germany, 2011-2013'

import math
import numpy as np
import oeqLookuptable as oeq
def get(*xin):


    l_lookup = oeq.lookuptable(
[
1849,1.368,
1850,1.368,
1851,1.37,
1852,1.37,
1853,1.37,
1854,1.37,
1855,1.37,
1856,1.355,
1857,1.332,
1858,1.305,
1859,1.275,
1860,1.245,
1861,1.218,
1862,1.195,
1863,1.18,
1864,1.173,
1865,1.173,
1866,1.176,
1867,1.18,
1868,1.182,
1869,1.182,
1870,1.181,
1871,1.18,
1872,1.18,
1873,1.179,
1874,1.18,
1875,1.18,
1876,1.18,
1877,1.18,
1878,1.18,
1879,1.18,
1880,1.18,
1881,1.18,
1882,1.18,
1883,1.18,
1884,1.18,
1885,1.18,
1886,1.18,
1887,1.18,
1888,1.18,
1889,1.18,
1890,1.18,
1891,1.18,
1892,1.18,
1893,1.18,
1894,1.18,
1895,1.18,
1896,1.18,
1897,1.18,
1898,1.18,
1899,1.18,
1900,1.18,
1901,1.18,
1902,1.18,
1903,1.18,
1904,1.18,
1905,1.181,
1906,1.181,
1907,1.18,
1908,1.179,
1909,1.178,
1910,1.178,
1911,1.18,
1912,1.184,
1913,1.188,
1914,1.188,
1915,1.18,
1916,1.162,
1917,1.136,
1918,1.104,
1919,1.07,
1920,1.036,
1921,1.004,
1922,0.978,
1923,0.96,
1924,0.952,
1925,0.952,
1926,0.956,
1927,0.96,
1928,0.962,
1929,0.962,
1930,0.961,
1931,0.96,
1932,0.959,
1933,0.959,
1934,0.96,
1935,0.96,
1936,0.96,
1937,0.961,
1938,0.961,
1939,0.96,
1940,0.959,
1941,0.958,
1942,0.958,
1943,0.96,
1944,0.965,
1945,0.976,
1946,0.995,
1947,1.026,
1948,1.07,
1949,1.129,
1950,1.192,
1951,1.248,
1952,1.285,
1953,1.29,
1954,1.256,
1955,1.19,
1956,1.104,
1957,1.01,
1958,0.919,
1959,0.837,
1960,0.772,
1961,0.73,
1962,0.714,
1963,0.716,
1964,0.725,
1965,0.73,
1966,0.723,
1967,0.706,
1968,0.682,
1969,0.655,
1970,0.629,
1971,0.606,
1972,0.589,
1973,0.58,
1974,0.58,
1975,0.583,
1976,0.585,
1977,0.58,
1978,0.563,
1979,0.536,
1980,0.504,
1981,0.47,
1982,0.438,
1983,0.409,
1984,0.386,
1985,0.37,
1986,0.363,
1987,0.362,
1988,0.365,
1989,0.37,
1990,0.374,
1991,0.375,
1992,0.374,
1993,0.37,
1994,0.362,
1995,0.352,
1996,0.341,
1997,0.33,
1998,0.321,
1999,0.312,
2000,0.304,
2001,0.295,
2002,0.285,
2003,0.275,
2004,0.266,
2005,0.26,
2006,0.26,
2007,0.26,
2008,0.26,
2009,0.26,
2010,0.261,
2011,0.261,
2012,0.26,
2013,0.26,
2014,0.26,
2015,0.26,
2016,0.26,
2017,0.26,
2018,0.26,
2019,0.26,
2020,0.26,
2021,0.26])
    return(l_lookup.lookup(xin))