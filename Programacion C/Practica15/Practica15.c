//Preprocesador
#include <sqlite3.h>
#include <stdio.h>
//programa principal
int main(void) {
    
    sqlite3 *db;
    char *err_msg = 0;
    //Se intenta abrir la base de datos Becarios.db, si no existe la crea.
    int rc = sqlite3_open("Becarios.db", &db);
    //si no se puede abrir la base de datos, muestra error.
    if (rc != SQLITE_OK) {
        
        fprintf(stderr, "No es posible abrir la base de datos: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
        
        return 1;
    }
    //Mensaje de que se pudo abrir la base de datos.
    printf("Conectado a la base de datos.\n");
    //Se inseran los datos, id como entero, nombre como texto, escuela como texto.
    char *sql = "DROP TABLE IF EXISTS Gen12;" 
                "CREATE TABLE Gen12(Id INT, Nombre TEXT, Escuela TEXT);" 
                "INSERT INTO Gen12 VALUES(1, 'Hugo','FCA');" 
                "INSERT INTO Gen12 VALUES(2, 'Carlos', 'FCA');" 
                "INSERT INTO Gen12 VALUES(3, 'Gerardo', 'FI');" 
                "INSERT INTO Gen12 VALUES(4, 'Rafa', 'FI');" 
                "INSERT INTO Gen12 VALUES(5, 'Marco', 'FC');" 
                "INSERT INTO Gen12 VALUES(6, 'Claudia', 'FC');" 
                "INSERT INTO Gen12 VALUES(7, 'Miguel', 'FI');" 
                "INSERT INTO Gen12 VALUES(8, 'Andrea', 'FC');"
		"INSERT INTO Gen12 VALUES(9,'Aline','FCA');"
		"INSERT INTO Gen12 VALUES(10,'Esteban','FI');"
		"INSERT INTO Gen12 VALUES(11,'Jairo','ESCOM');"
		"INSERT INTO Gen12 VALUES(12,'Samuel','ESCOM');"
		"INSERT INTO Gen12 VALUES(13,'Jose','ESCOM');"
		"INSERT INTO Gen12 VALUES(14,'Guadalupe','UPIITA');"
		"INSERT INTO Gen12 VALUES(15,'Angel','FI');"
		"INSERT INTO Gen12 VALUES(16,'Ulises','FI');";
    //mensajes de error
    rc = sqlite3_exec(db, sql, 0, 0, &err_msg);
    
    if (rc != SQLITE_OK ) {
        
        fprintf(stderr, "SQL error: %s\n", err_msg);
        
        sqlite3_free(err_msg);        
        sqlite3_close(db);
        
        return 1;
    } 
    //mensaje de insercion de datos correcta.
    printf("Datos insertados correctamente en la base de datos.\n");
    //se cierra la base de datos.
    sqlite3_close(db);
    
    return 0;
}
