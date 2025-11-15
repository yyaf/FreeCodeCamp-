import re

def update_progress(md_file="readme.md"):
    # 读取 Markdown 文件
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 匹配任务复选框
    total_tasks = len(re.findall(r"- \[.\]", content))
    completed_tasks = len(re.findall(r"- \[x\]", content, re.IGNORECASE))

    # 计算进度
    remaining_tasks = total_tasks - completed_tasks
    completion_rate = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # 生成进度条（20 格）
    bar_length = 20
    filled_length = int(bar_length * completed_tasks // total_tasks)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)

    # 构建进度统计文本
    progress_text = (
        "## 学习进度统计\n\n"
        f"- 总任务数：{total_tasks}\n"
        f"- 已完成：{completed_tasks}\n"
        f"- 剩余：{remaining_tasks}\n"
        f"- 完成率：{completion_rate:.2f}%\n\n"
        f"### 可视化进度条\n"
        f"[{bar}] 完成率：{completion_rate:.2f}%\n"
    )

    # 替换或追加进度统计部分
    if "## 学习进度统计" in content:
        content = re.sub(r"## 学习进度统计[\\s\\S]*?(?=\\n#|\\Z)", progress_text, content)
    else:
        content += "\n\n" + progress_text

    # 写回文件
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{completed_tasks}✅ 已更新 readme.md 中的进度统计表！")

if __name__ == "__main__":
    update_progress("readme.md")
