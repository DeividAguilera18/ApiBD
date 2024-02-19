from fastapi import APIRouter, HTTPException, status
from models import models
from install import connect

router = APIRouter()

@router.get('/movies')
def get_movies():

    temporal_list= []

    with connect.con.cursor() as cursor:
        try:
            get_data_query = f'''
            SELECT * FROM my_movies 
            '''

            print(get_data_query)
            cursor.execute(get_data_query)
            rows = cursor.fetchall()

            for row in rows:
                print(row)
                temporal_list.append(row)

        except Exception as e:
            print(f"Error: {e}")
    return {"message": temporal_list}


@router.post('/movies')
def create_movies(mov:models.Movie):
    print(mov.Autor)
    print(mov.Descripcion)
    print(mov.Fecha_de_Estreno)

    with connect.con.cursor() as cursor:
        try:
            insert_data_query = f'''
            INSERT INTO my_movies (Autor, Descripcion, Fecha_de_Estreno)  VALUES (%s, %s, %s);
            '''

            data_to_insert = (mov.Autor, mov.Descripcion, mov.Fecha_de_Estreno)
            print(data_to_insert)
            cursor.execute(insert_data_query, data_to_insert)
            rows = cursor.fetchall()
            connect.con.commit()

          

        except Exception as e:
            print(f"Error: {e}")

    return {"message": "Pelicula agregada correctamente"}

# Método PUT para actualizar datos de la BD
@router.put('/movies/{movie_id}')
def update_movie(movie_id: int, movie: models.Movie):
    with connect.con.cursor() as cursor:
        try:
            # Verificar si la película existe
            cursor.execute("SELECT * FROM my_movies WHERE ID = %s", (movie_id,))
            existing_movie = cursor.fetchone()
            if existing_movie is None:
                raise HTTPException(status_code=404, detail="Película no encontrada")

            # Actualizar los campos de la película
            update_query = """
                UPDATE my_movies
                SET Autor = %s, Descripcion = %s, Fecha_de_Estreno = %s
                WHERE ID = %s
            """
            cursor.execute(update_query, (movie.Autor, movie.Descripcion, movie.Fecha_de_Estreno, movie_id))
            connect.con.commit()

            return {"message": "Película actualizada correctamente"}

        except Exception as e:
            print(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")


# Método DELETE para borrar datos de la BD
@router.delete('/movies/{movie_id}')
def delete_movie(movie_id: int):
    with connect.con.cursor() as cursor:
        try:
            # Verificar si la película existe
            cursor.execute("SELECT * FROM my_movies WHERE ID = %s", (movie_id,))
            existing_movie = cursor.fetchone()
            if existing_movie is None:
                raise HTTPException(status_code=404, detail="Película no encontrada")

            # Eliminar la película
            delete_query = "DELETE FROM my_movies WHERE ID = %s"
            cursor.execute(delete_query, (movie_id,))
            connect.con.commit()

            return {"message": "Película eliminada correctamente"}

        except Exception as e:
            print(f"Error: {e}")
            raise HTTPException(status_code=500, detail="Error interno del servidor")
