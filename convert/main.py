def clicked_on(self):
    RUB = {"USD": 0.011, "EURO": 0.01, "CNY": 0.08}
    USD = {"RUB": 90, "EURO": 0.92, "CNY": 7.2}
    EURO = {"USD": 1.08, "RUB": 97, "CNY": 7.81}
    CNY = {"USD": 0.14, "EURO": 0.12, "RUB": 12.44}

    dic_1 = {"RUB": RUB, "USD": USD, "EURO": EURO, "CNY": CNY}
    currency_1 = self.first.currentText()
    currency_2 = self.second.currentText()
    value = float(self.currency.text())

    if currency_1 == currency_2:
        return value
    for key_u, value_e in dic_1.items():
        if key_u == currency_2:
            #good
            good = value_e
            for key, value_i in good.items():
                if key == currency_1:
                    res = value / value_i
                    return res
        else:
            continue






