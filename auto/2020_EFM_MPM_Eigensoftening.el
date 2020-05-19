(TeX-add-style-hook
 "2020_EFM_MPM_Eigensoftening"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("elsarticle" "preprint" "12pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("amsmath" "fleqn" "tbtags") ("algorithm2e" "linesnumbered" "ruled" "vlined") ("glossaries" "acronym")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "elsarticle"
    "elsarticle12"
    "lineno"
    "hyperref"
    "float"
    "graphicx"
    "subfigure"
    "color"
    "soul"
    "cancel"
    "amsmath"
    "mathtools"
    "amsthm"
    "amssymb"
    "xstring"
    "algorithm2e"
    "glossaries")
   (TeX-add-symbols
    '("Deriv" ["argument"] 2)
    '("Integral" 2)
    '("GradT" 1)
    '("GradS" 1)
    '("Grad" 1)
    '("Div" 1)
    '("Vector" 1)
    '("Matrix" 1)
    '("tens" 1)
    '("vect" 1))
   (LaTeX-add-labels
    "sec:1"
    "sec:2"
    "sec:2.1"
    "eq:Predictor-velocity"
    "eq:Corrector-velocity"
    "eq:Update-lagrangian-pce"
    "sec:2.2"
    "eq:LME-scheme-pareto-set"
    "eq:LME-p"
    "eq:LME-Z"
    "eq:LME-gradp"
    "eq:LME-J"
    "eq:LME-r"
    "sec:2.3"
    "eq:energy-release-EE"
    "fig:Failed-particles"
    "fig:Damage-ft-wc"
    "eq:variation-averaged-strain-energy-density"
    "eq:variation-averaged-strain-energy-density-simpli"
    "eq:equivalent-critical-stress"
    "eq:averaged-mass"
    "eq:f-int-damaged"
    "eq:damaged-variable-chi"
    "eq:effective-fracture-strain"
    "eq:damage-variable-chi-II"
    "eq:damage-variable-chi-III"
    "sec:3"
    "sec:edge-cracked-square-I"
    "fig:geometry-cracked-panel-mode-I"
    "fig:Reactions-cracked-panel-mode-I"
    "fig:Stress-cracked-panel-mode-I"
    "sec:3.3"
    "fig:geometry-drop-weight-impact-test"
    "sec:4"
    "sec:expl-pred-corr"
    "sec:eigens-algor-1"
    "alg-eigens")
   (LaTeX-add-bibliographies
    "Biblio"))
 :latex)

