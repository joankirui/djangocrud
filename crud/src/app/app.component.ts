import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  movies = [{title: 'Test'}];
  selectedMovie: any;

  constructor(private api: ApiService) {
    this.getMovies();
    this.selectedMovie = {id: -1, title: '', description: '', year: 0};
  }
  getMovies(){
    this.api.getAllMovies().subscribe(
      (data: any) => {
        this.movies = data;

      },
      (error: any) => {
        console.log(error);
      }

    );
  }
  movieClicked(film:any){
    this.api.getOneMovie(film.id).subscribe(
      (data: any) => {
        this.selectedMovie = data;

      },
      (error: any) => {
        console.log(error);
      }

    );
  }
  updateMovie(){
    this.api.updateMovie(this.selectedMovie).subscribe(
      (data: any) => {
        this.getMovies();

      },
      (error: any) => {
        console.log(error);
      }

    );

  }
  createMovie(){
    this.api.createMovie(this.selectedMovie).subscribe(
      (data: any) => {
        this.movies.push(data);

      },
      (error: any) => {
        console.log(error);
      }

    );

  }
  deleteMovie(){
    this.api.deleteMovie(this.selectedMovie.id).subscribe(
      (data: any) => {
        this.getMovies();

      },
      (error: any) => {
        console.log(error);
      }

    );

  }
}
