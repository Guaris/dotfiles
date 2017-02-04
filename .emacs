
;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["#242424" "#e5786d" "#95e454" "#cae682" "#8ac6f2" "#333366" "#ccaa8f" "#f6f3e8"])
 '(custom-enabled-themes (quote (wombat)))
 '(custom-safe-themes
   (quote
    ("9f9d163bff5db858e1049a9ab1661e81c32ddc723b81910305119bc9deee1f30" default)))
 '(inhibit-startup-screen t)
 '(package-selected-packages (quote (sx ## flycheck neotree))))
 '(package-archives
   (quote
    (("gnu". "http://elpa.gnu.org/packages/")
     ("melpa" . "http://melpa.org/packages/"))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
;;kill startup screen

;;;
(require 'ido)
(ido-mode t)
;;package archives
(add-to-list 'package-archives
	     '("melpa" . "http://melpa.org/packages/"))
;;Global-Flycheck mode
(add-hook 'after-init-hook #'global-flycheck-mode)
;;;Melpa round two
(add-to-list 'package-archives
	     '("melpa" . "https://melpa.org/packages/") t)
