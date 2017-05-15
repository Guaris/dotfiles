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
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["#242424" "#e5786d" "#95e454" "#cae682" "#8ac6f2" "#333366" "#ccaa8f" "#f6f3e8"])
 '(custom-enabled-themes (quote (grandshell)))
 '(custom-safe-themes
   (quote
    ("cd560f7570de0dcdcf06953b3f1a25145492a54f100f9c8da3b4091b469f7f02" "9f9d163bff5db858e1049a9ab1661e81c32ddc723b81910305119bc9deee1f30" default)))
 '(inhibit-startup-screen t)
 '(markdown-command "/usr/local/bin/pandoc")
 '(package-selected-packages
   (quote
    (magit markdown-mode+ markdown-preview-mode markdown-preview-eww grandshell-theme auctex langtool w3 sx ## flycheck neotree))))
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
	     '("melpa-archives" . "http://stable.melpa.org/packages/") t)
	    
;;Global-Flycheck mode
(add-hook 'after-init-hook #'global-flycheck-mode)
;;;Melpa round two
(add-to-list 'package-archives
	     '("melpa" . "https://melpa.org/packages/") t)
;;; org-mode config
;;Enable Org-mode
(require 'org)
;;Make org-mode work with files ending in.org
(add-to-list 'auto-mode-alist '("\\.org$" . org-mode))
(define-key global-map "\C-cl" 'org-store-link)
(define-key global-map "\C-ca" 'org-agenda)
(setq org-log-done t)

;;;orgmode clock persisting for clock-ins
(setq org-clock-persist 'history)
(org-clock-persistence-insinuate)

;;;Langtool config
(require 'langtool)
(setq langtool-language-tool-jar "/users/angel/Documents/LanguageTool-3.7/languagetool.jar")
(setq langtool-mother-tounger "en")
;;Hooking Flyspell into orgmode
(add-hook 'org-mode-hook 'flyspell-mode)
(add-hook 'org-mode-hook 'flyspell-buffer)
;;ignore flags
(setq flyspell-issue-message-flag nil)
(add-hook 'org-mode-hook (lambda () (setq ispell-parser 'tex)))
(defun flyspell-ignore-tex()
  (interactive)
  (set(make-variable-buffer-local 'ispell-parser) 'tex))
(add-hook 'org-mode-hook 'flyspell-ignore-tex)
;;;count words
(add-hook 'org-mode-hook 'wc-mode)
(add-hook 'org-mode-hook 'turn-on-org-cdlatex)
(add-hook 'markdown-mode-hook 'pandoc-mode)



;;path for tex
(setenv "PATH" "/usr/local/bin:/Library/TeX/texbin/:$PATH" t)
(setq exec-path (append exec-path '("/Library/TeX/texbin")))


(add-hook 'org-mode-hook #'(lambda ()

                             ;; make the lines in the buffer wrap around the edges of the screen.

                             ;; to press C-c q  or fill-paragraph ever again!
                             (visual-line-mode)
                             (org-indent-mode)))
;;;org agenda aat startup
(setq org-agenda-files (list "~/org/work.org"
                             "~/org/school.org")) 
                             
(add-hook 'after-init-hook 'org-agenda-list)
