def organize_questions(input_file, output_file, separator="::"):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            questions = []
            current_question = ""
            for line in lines:
                line = line.strip()
                if line:
                    if line.endswith(separator):
                        current_question += line
                    else:
                        current_question += line + "\n"
                else:
                    questions.append(current_question.strip())
                    current_question = ""

            if current_question:
                questions.append(current_question.strip())

        with open(output_file, 'w', encoding='utf-8') as f:
            for idx, question in enumerate(questions):
                f.write(f"Question {idx + 1}:\n")
                f.write(question + "\n\n")
        print(f"题库整理完成，共整理了{len(questions)}道题目。")
    except FileNotFoundError:
        print("文件不存在，请检查文件路径。")


if __name__ == "__main__":
    input_file_path = input("请输入原始题库文件路径：")
    output_file_path = input("请输入整理后的题库文件路径：")
    separator = input("请输入问题和答案的分隔符（默认为'::'）：") or "::"
    organize_questions(input_file_path, output_file_path, separator)
