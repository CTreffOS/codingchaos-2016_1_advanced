import Data.Char

key = "chaostreffosnabrueck"

offset :: Char -> Int
offset x = (ord x) - 97

alphabet = "abcdefghijklmnopqrstuvwxyz"

shift :: (Char, Char) -> Char
shift (a, b) = if (b `elem` alphabet) then (chr $ 97 + (offset a + offset b) `mod` 26) else b

encode :: String -> String
encode = map shift . zip (concat $ repeat key)

main = do
  line <- getLine
  print $ encode line
