letter = '''Dear <|Name|>,
             You are selected!
                <|Date|> '''

print(letter.replace("<|Name|>", "Ankit").replace("<|Date|>", "03 july 2025"))
