from lib import lib

lib messagebird.tel.available --country <CA>
lib messagebird.tel.init --number <available phone number>

result = lib.messagebird.tel['@0.0.20'].init({
  "number": None # (required)
})