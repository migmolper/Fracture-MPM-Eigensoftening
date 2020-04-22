(TeX-add-style-hook
 "MPM_fracture"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("subfig" "lofdepth" "lotdepth") ("units" "ugly")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "subfig"
    "graphicx"
    "subcaption"
    "subfigure"
    "mathptmx"
    "amssymb"
    "amsmath"
    "amsfonts"
    "epstopdf"
    "mathrsfs"
    "hyperref"
    "enumitem"
    "array"
    "tabularx"
    "supertabular"
    "fancyhdr"
    "multirow"
    "color"
    "makeidx"
    "xstring"
    "setspace"
    "epsfig"
    "pgf"
    "preview"
    "algorithm"
    "algorithmic"
    "algpseudocode"
    "stanli"
    "units")
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
    '("vec" 1))
   (LaTeX-add-labels
    "intro"
    "sec:meshfree-methodology"
    "sec:spat-discr"
    "eq:Shannon-entropy"
    "eq:least-biased-approximation-scheme"
    "eq:LME-scheme-pareto-set"
    "eq:LME-p"
    "eq:LME-Z"
    "eq:LME-grad-p"
    "eq:LME-f"
    "eq26"
    "eq27"
    "eq28"
    "sec:temp-discr"
    "eq:Predictor-velocity-I"
    "eq:Variational-recovery"
    "eq:Predictor-velocity-II"
    "eq:Corrector-velocity"
    "eq:Update-lagrangian-pce"
    "sec:eigens-algor"
    "eq:energy-release-EE"
    "fig:Damage-ft-wc"
    "eq:variation-averaged-strain-energy-density"
    "eq:variation-averaged-strain-energy-density-simpli"
    "eq:equivalent-critical-stress"
    "sec:cases-study"
    "sec:comp-with-analyt"
    "sec:braz-test"
    "fig:geometry-brazilian-test"
    "sec:drop-weight-impact"
    "fig:geometry-drop-weight-impact-test"
    "sec:expl-pred-corr"
    "sec:eigens-algor-1"
    "alg-eigens")
   (LaTeX-add-bibliographies
    "Biblio/Biblio"))
 :latex)

