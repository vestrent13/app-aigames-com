def generate_site_summary():
    site_data = {
        "title": "爱游戏",
        "url": "https://app-aigames.com",
        "keywords": ["爱游戏", "h5游戏", "在线游戏", "休闲游戏", "网页游戏"],
        "tags": ["游戏平台", "HTML5", "娱乐", "互动"],
        "description": "爱游戏是一个专注于H5游戏的在线平台，提供丰富多样的休闲与互动游戏体验。"
    }

    summary_parts = []

    summary_parts.append("=== 站点摘要 ===")
    summary_parts.append(f"站点名称：{site_data['title']}")
    summary_parts.append(f"访问地址：{site_data['url']}")
    summary_parts.append(f"简短说明：{site_data['description']}")

    keywords_str = "、".join(site_data["keywords"])
    summary_parts.append(f"核心关键词：{keywords_str}")

    tags_str = "、".join(site_data["tags"])
    summary_parts.append(f"关联标签：{tags_str}")

    summary_parts.append(f"关键词数量：{len(site_data['keywords'])}")
    summary_parts.append(f"标签数量：{len(site_data['tags'])}")

    url_length = len(site_data["url"])
    summary_parts.append(f"URL长度：{url_length} 字符")

    if "爱游戏" in site_data["keywords"]:
        summary_parts.append("备注：关键词列表包含'爱游戏'。")

    if "游戏平台" in site_data["tags"]:
        summary_parts.append("备注：标签包含'游戏平台'分类。")

    summary_parts.append("=" * 25)

    return "\n".join(summary_parts)


def format_summary_as_block(text):
    lines = text.split("\n")
    block = []
    for line in lines:
        block.append(f"| {line}")
    return "\n".join(block)


def count_summary_stats(text):
    lines = text.split("\n")
    non_empty = [l for l in lines if l.strip()]
    return {
        "total_lines": len(lines),
        "non_empty_lines": len(non_empty),
        "char_count": len(text),
        "word_count": len(text.split()),
    }


def show_summary_with_stats():
    summary = generate_site_summary()
    print(summary)
    print()
    stats = count_summary_stats(summary)
    print("=== 摘要统计 ===")
    print(f"总行数：{stats['total_lines']}")
    print(f"非空行数：{stats['non_empty_lines']}")
    print(f"总字符数：{stats['char_count']}")
    print(f"总单词数：{stats['word_count']}")
    print("=" * 25)


def export_summary_to_list():
    summary = generate_site_summary()
    return summary.split("\n")


def main():
    print("开始生成站点摘要...\n")
    show_summary_with_stats()
    print("\n摘要已生成完毕。")


if __name__ == "__main__":
    main()