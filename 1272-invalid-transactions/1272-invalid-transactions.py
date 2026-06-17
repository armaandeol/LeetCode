class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        by_name = defaultdict(list)


        for idx, t in enumerate(transactions):
            name, time, amount, city = t.split(",")

            trans = {
                "name": name,
                "time": int(time),
                "amount": int(amount),
                "city": city,
                "raw": t,
                "idx": idx
            }

            parsed.append(trans)
            by_name[name].append(trans)

        invalid = set()


        for trans in parsed:
            if trans["amount"] > 1000:
                invalid.add(trans["idx"])

            for other in by_name[trans["name"]]:

                if trans["idx"] == other["idx"]:
                    continue

                if (trans["city"] != other["city"] and
                    abs(trans["time"] - other["time"]) <= 60):

                    invalid.add(trans["idx"])
                    break

        return [transactions[i] for i in invalid]