from unstructured.partition.pdf import partition_pdf

def extract_text(file_path)->str:
  # extract elements from pdf
  elements = partition_pdf(filename=file_path, strategy="hi_res")

  # list of element types not allowed
  not_allowed_elements = ['FigureCaption', 'Image', 'Table', 'Footer']
  text = ""
  for element in elements:
    if element.to_dict()['type'] not in (not_allowed_elements):
      text += str(element) + "\n"
  return text



if __name__ == "__main__":
  SAMPLE_TEXT_FOR_BENCH = extract_text(file_path='data/etl_sample.pdf')
  print(SAMPLE_TEXT_FOR_BENCH)