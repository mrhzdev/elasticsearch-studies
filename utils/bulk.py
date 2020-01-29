#!/usr/bin/python3
import sys, os, getopt, json

def main():

  file, _index, _type, _id = read_params()

  full_path = "%s/%s" % (os.getcwd(),file)

  if os.path.isfile(full_path) is False:
    print('File not exists, going to process')
    sys.exit(1)

  data = read_file(full_path)

  process_data(data,_index,_type,_id)


  # print('file  : ', end="")
  # print(file)

  exit(1)

  print('_index: ', end="")
  print(_index)
  print('_type : ', end="")
  print(_type)
  print('_id   : ', end="")
  print(_id)

  pass

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
    with open(path) as json_file:
      data = json.load(json_file)
  except:
    print('Error on load json file!')
    sys.exit(2)

  return data

def process_data(data,_index,_type,_id):

  rs = _id.split('.')

  print(rs)

  # print(_index,_type,_id)
  # print(data)
  pass


if __name__ == "__main__":
  main()
