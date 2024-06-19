#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @created: 02.02.2024
# @author: Aleksey Komissarov
# @author: Claude Opus
# @contact: ad3002@gmail.com

import os
import argparse

def traverse_repository(repo_path, extensions):
    code_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                code_files.append(file_path)
    return code_files

def extract_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    return code

def consolidate_code_xml(code_files):
    consolidated_code = ""
    for file_path in code_files:
        code = extract_code(file_path)
        instruction = f"<file>\n<path>{file_path}</path>\n<content>\n{code}\n</content>\n</file>\n\n"
        consolidated_code += instruction
    return consolidated_code

def consolidate_code_raw(code_files):
    consolidated_code = ""
    for file_path in code_files:
        code = extract_code(file_path)
        instruction = f"###### {file_path} ###\n{code}\n###### end of file {file_path} ###\n\n"
        consolidated_code += instruction
    return consolidated_code

def main():
    parser = argparse.ArgumentParser(description="Code Consolidator")
    parser.add_argument("-r", "--repo_path", help="Path to the code repository", required=True)
    parser.add_argument("-o", "--output_file", default="consolidated_code.code", help="Output file (default: consolidated_code.code)")
    parser.add_argument("-f", "--format", default="xml", help="Output format xml, raw (default: xml)")
    parser.add_argument("-e", "--extensions", nargs="+", default=[".py"], help="File extensions to include (default: .py)")
    args = parser.parse_args()

    repo_path = args.repo_path
    extensions = args.extensions
    output_file = args.output_file
    format = args.format

    if not format in ["xml", "raw"]:
        raise ValueError("Invalid format. Choose from xml, raw")

    code_files = traverse_repository(repo_path, extensions)
    if format == "xml":
        consolidated_code = consolidate_code_xml(code_files)
    elif format == "raw":
        consolidated_code = consolidate_code_raw(code_files)
    
    with open(output_file, "w") as file:
        file.write(consolidated_code)

if __name__ == "__main__":
    main()