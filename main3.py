class TextModifier:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        match args[0]:
            case 0:
                result = self.func(self, *args, **kwargs)
                new_result = result.lower()
                return new_result

            case 1:
                result = self.func(self, *args, **kwargs)
                new_result = result.upper()
                return new_result

            case 2:
                result = self.func(self, *args, **kwargs)
                new_result = ""

                for value in result:
                    if value == " ":
                        continue
                    new_result += value

                return new_result

            case 3:
                result = self.func(self, *args, **kwargs)
                new_result = ""

                shift = int(input("Enter shift: "))
                j = 0

                for i in range(len(result)):
                    if i + shift < len(result):
                        new_result += result[i + shift]

                    else:
                        new_result += result[j]
                        j += 1

                return new_result


@TextModifier
def strer(*args, **kwargs):
    return "Hello World"


print(strer(3))