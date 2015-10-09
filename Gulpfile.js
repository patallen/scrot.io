var gulp = require('gulp')
var sass = require('gulp-sass')

gulp.task('sass', function () {
  gulp.src('./static/sass/**/*.sass')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('static/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./static/sass/**/*.sass', ['sass']);
});