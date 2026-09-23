# 两条命令，没有别的。
.PHONY: help data readme all

help:
	@echo "make data     # 从 GitHub 刷新 data/stars.json（需要 GITHUB_TOKEN）"
	@echo "make readme   # 由 data/ 重新生成 README.md / README.zh-CN.md / banner"
	@echo "make all      # 先 data 再 readme —— 这就是全部流程"

data:
	python3 scripts/fetch_stars.py

readme:
	python3 scripts/gen_readme.py

all: data readme
