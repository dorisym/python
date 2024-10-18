import readdocx

content = readdocx.read_docx_content_with_tables("./20241016203218.docx")
print(content)