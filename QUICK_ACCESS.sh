#!/bin/bash
# Stage 3 项目快速访问脚本

echo "=== Stage 3 项目快速访问 ==="
echo ""
echo "选择项目:"
echo "1) P01 医院销售分析"
echo "2) P02 服装零售RFM分析"
echo "3) P03 银行营销分类预测"
echo "4) 查看所有项目"
echo "5) 查看项目文档"
echo ""
read -p "请输入选项 (1-5): " choice

case $choice in
  1)
    cd specs/002-ai-tutorial-stages/docs/stage3/projects/p01-healthcare
    echo "已进入 P01 医院销售分析项目"
    ls -la
    ;;
  2)
    cd specs/002-ai-tutorial-stages/docs/stage3/projects/p02-ecommerce
    echo "已进入 P02 服装零售RFM分析项目"
    ls -la
    ;;
  3)
    cd specs/002-ai-tutorial-stages/docs/stage3/projects/p03-bank-marketing
    echo "已进入 P03 银行营销分类预测项目"
    ls -la
    ;;
  4)
    tree -L 2 specs/002-ai-tutorial-stages/docs/stage3/projects/
    ;;
  5)
    cat STAGE3_PROJECTS.md
    ;;
  *)
    echo "无效选项"
    ;;
esac
