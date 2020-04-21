(TeX-add-style-hook
 "Drop_weight"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("standalone" "border=10pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("pstricks" "pdf")))
   (TeX-run-style-hooks
    "latex2e"
    "standalone"
    "standalone10"
    "pstricks"))
 :latex)

