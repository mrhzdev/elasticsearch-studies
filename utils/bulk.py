#!/usr/bin/python3
import sys, os, getopt, json

def main():

  file, _index, _type, _id = read_params()

  full_path = "%s/%s" % (os.getcwd(),file)

  if os.path.isfile(full_path) is False:
    print('File not exists, going to process')
    sys.exit(1)

  data = read_file(full_path)

  x_ndjson = process_data(data,_index,_type,_id)

  # put out bulk data
  print("\n".join(x_ndjson))

def usage():
  script_name = sys.argv[0]
  print("""Usage: %s [OPTION]...\n
    -f, --file  <file_path> File path thats will be read ( required )
    -i, --index <_index>    Elasticsearch index
    -t, --type  <_type>     Elasticsearch type
    -d, --id    <_id>       Converts a json path (element.propertie.id) to elasticsearch Id
        --help              Display this help and exit
  """ % (script_name))
  sys.exit(1)

def read_params():
  try:
    opts, args = getopt.getopt(sys.argv[1:], "f:i:t:d:h", ["file=","index=", "type=", "id=", "help"])

  except getopt.GetoptError as err:
    script_name = sys.argv[0]
    print( "%s %s" % (script_name, str(err)))  # will print something like "option -a not recognized"
    print( "Try '%s -h' or '%s --help' for more information." % (script_name,script_name))
    sys.exit(2)

  file = None
  _index = None
  _type = None
  _id = None

  for o, a in opts:
    if o in ("-h", "--help"):
      usage()
    elif o in ("-f", "--file"):
      file = a
    elif o in ("-i", "--index"):
      _index = a
    elif o in ("-t", "--type"):
      _type = a
    elif o in ("-d", "--id"):
      _id = a
    else:
      assert False, "unhandled option"

  if file is None:
    print("'--file' or '-f' params is required\n")
    usage() 

  return file, _index, _type, _id

def read_file(path):

  try:
    with open(path,encoding='utf-8') as json_file:
      data = json.load(json_file)
  except:
    print('Error on load json file!')
    sys.exit(2)

  return data

def process_data(data,_index,_type,id_path):

  x_ndjson = []

  sample_idx = {}

  if _index is not None:
    sample_idx['_index'] = _index
  if _type is not None:
    sample_idx['_type'] = _type

  for el in data:

    _id = None
    reg = el

    if id_path is not None:
      _id, reg = get_id(id_path.split('.'),el)

    idx = sample_idx.copy()

    if _id is not None:
      idx['_id'] = _id

    x_ndjson.append(json.dumps({'index':idx}))
    x_ndjson.append(json.dumps(reg,ensure_ascii=False))

  return x_ndjson

def get_id(id_path,data):

  key = id_path[0]

  if len(id_path) == 1:

    if key not in data:
      print("Key '%s' not exists in array, check the json path to id." % key)
      sys.exit(2)
    else:

      _id = data[key]
      del data[key]

      if _id is None or _id == '' or isinstance( _id, dict ) :
        print("ID is invalid")
        sys.exit(2)

      return _id, data
  else:
    if key in data and isinstance( data[key], dict ):
      _id, nData = get_id(id_path[1:],data[key])

      if len(nData) == 0:
        del data[key]
      
      return _id, data

    else:
      print("Key path '%s' not exists in array, check the path to id." % '.'.join(id_path))
      sys.exit(2)

if __name__ == "__main__":
  main()
