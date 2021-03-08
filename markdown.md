# Sec 1

## Sec 1.1

The *quick 斜体* brown fox jumps over the **lazy 加粗** dog.  
==高亮文字==

**Ctrl+Shift+V 预览结果。**

第三，Markdown 在显示时会被预览工具翻译为 HTML。
比如

### XXX

会被翻译为

<h3>XXX</h3>

Markdown 是 HTML 的一种简写，在显示时会『解压缩』成 HTML。
理论上你可以在 Markdown 里直接插入合法的 HTML 块，
他们会成为最终的 HTML 的一部分，做到 Markdown 本身做不到的事。 （不空行视为一段话，即使enter了。）

---
分割线

无序列表
* 1
* 2
* * 2
* * 7

1. 有序列表
1. 不需要
1. 前面按照数字排列，可以随意调换顺序

>\>开头的行被认为是一段引用的文字


    前面空四格的段落被认为是code section (内容不会被解释成任何格式)
    (define (make-adder num)
      (define (foo x)
              (+ x num))
      foo)


```scheme

(define x (cons 1 2))
x
(car x)
(cdr x)

;return length
(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

;return which item
(define (getitem items n)
  (if (= n 0)
      (car items)
      (getitem (cdr items) (- n 1))))
```

插入目录
[TOC]
 
L ^A^ TEX :smile:

http://criticmarkup.com/users-guide.php

Addition {++ ++}
Deletion {-- --}
Substitution {~~ ~> ~~}
Comment {>> 哈哈 <<}
Highlight {== ==}{>> <<}

@import "lisp.md"


 hahahah ``inline code``