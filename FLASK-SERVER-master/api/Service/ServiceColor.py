class ServiceColor:
    @staticmethod
    def get_color(color) -> str:
        try:

            if color == (-16777216):
                color = str('#010101')

            elif color == (-10453621):
                color = str('#6B8879')

            elif color == (-6381922):
                color = str('#535453')

            elif color == (-8825528):
                color = str('#B1733D')

            elif color == (-43230):
                color = str('#FF7300')

            elif color == (-26624):
                color = str('#FFBF00')

            elif color == (-3285959):
                color = str('#FFBF00')

            elif color == (-7617718):
                color = str('#27A54C')

            elif color == (-11751600):
                color = str('#2AAD44')

            elif color == (-16738680):
                color = str('#4caf7f')

            elif color == (-16728876):
                color = str('#0A7CAD')

            elif color == (-16537100):
                color = str('#0A7CAD')

            elif color == (-14575885):
                color = str('#0A7CAD')

            elif color == (-12627531):
                color = str('#0A7CAD')

            elif color == (-10011977):
                color = str('#673ab7')

            elif color == (-6543440):
                color = str('#9c27b0')

            elif color == (-1499549):
                color = str('#ff2500')

            elif color == (-769226):
                color = str('#f95b49')

            elif color == (-65281):
                color = str('#dd28ff')
            elif color == (-16121):
                color = str('#F7AE01')

            elif color == (-5317):
                color = str('#F7AE01')

            elif color == 0:
                color = str('#5C6569')

            return color

        except Exception as e:

            print('Color_Class_Service', e)
            pass
