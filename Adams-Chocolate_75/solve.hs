sumd :: Int -> Int
sumd n
    | n < 10    = n
    | otherwise = n `mod` 10 + sumd (n `div` 10)

isSquare :: Int -> Bool
isSquare n = sq * sq == n
    where sq = floor $ sqrt $ (fromIntegral n::Double)

-- n - low - high - result
binarySearchCube :: Int -> Int -> Int -> Bool
binarySearchCube n low high
    | low >= high     = False
    | n == midCube    = True
    | n < midCube     = binarySearchCube n low (mid - 1)
    | n > midCube     = binarySearchCube n (mid + 1) high
        where mid = (high + low) `div` 2
              midCube = mid ^ 3

-- perform binary search on 1-n basically...
isCube :: Int -> Bool 
isCube n = binarySearchCube n 1 n

-- we store dates in the format
-- yyyymmdd
incrementDate :: Int -> Int
incrementDate date
    | days == 29 && month == 2 = year * 10000 + 301
    | days == 30 && days30 = year * 10000 + (month + 1) * 100 + 1
    | days == 31 && days31 = year * 10000 + (month + 1) * 100 + 1
    | otherwise = date + 1
        where year = date `div` 10000
              month = (date `mod` 10000) `div` 100
              days = date `mod` 100
              days30 = month `elem` [2, 4, 6, 9, 11]
              days31 = month `elem` [1, 3, 5, 7, 8, 10, 12]

getMonth :: Int -> Int
getMonth n = (n `mod` 10000) `div` 100

getYear :: Int -> Int
getYear n = n `div` 10000

saleBars :: Int -> Int
saleBars date
    | isSquare dateSum  = 0
    | isCube dateSum    = 0
    | date == 20161225  = 0
    | otherwise         = dateSum
        where dateSum = sumd date

getAnswer :: Int -> Int -> Int
getAnswer 20161301 bars = bars
getAnswer date bars = getAnswer (incrementDate date) (bars + (saleBars date))

main = do
    print (getAnswer 20160101 0)
