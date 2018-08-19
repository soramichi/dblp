(load "##first##_##last##_data.lsp")

(defun neq (x y) (not (eq x y)))

(defun author-position (author data)
  (mapcar
   (lambda (datum)
     (let ((pos (position-if (lambda (x) (equal author x)) (car datum))))
       (cond ((eq pos nil) -1) (t pos))))
   data))

(defun list-publication-iter (data author-positions pred lst)
  (cond
   ((eq author-positions nil) lst)
   (t (list-publication-iter (cdr data) (cdr author-positions) pred (cond
                                                                     ((funcall pred (car author-positions)) (cons (cdar data) lst))
                                                                     (t lst))))))

(defun list-publication (author data pred)
  (list-publication-iter data (author-position author data) pred '())
  )

(princ "1st-author papers:")
(print (list-publication "##first## ##last##" data (lambda (x) (eq x 0))))

(princ #\Newline)
(princ #\Newline)
(princ "Other papers:")
(print (list-publication "##first## ##last##" data (lambda (x) (neq x 0))))

(princ #\Newline)
(quit)
