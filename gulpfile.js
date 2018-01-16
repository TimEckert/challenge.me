var gulp = require('gulp');
var browserSync = require('browser-sync');
var reload = browserSync.reload;
var sass = require('gulp-sass');


gulp.task('scss', function() {
    gulp.src('scss/main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('css/'))
        .pipe(reload({stream:true}));
});

gulp.task('html', function() {
    gulp.src('index.html')
        .pipe(reload({stream:true}));
});

gulp.task('browser', function () {
    browserSync({
        server: {
            baseDir: './'
        }
    });
});

//Watch task
gulp.task('default', ['scss','browser'] ,function() {
    gulp.watch('scss/*.scss',['scss']);
    gulp.watch('index.html',['html']);
});
