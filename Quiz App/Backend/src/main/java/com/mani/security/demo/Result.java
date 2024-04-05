package com.mani.security.demo;

import org.springframework.stereotype.Component;

import jakarta.annotation.Generated;
import jakarta.persistence.Entity;
import jakarta.persistence.EntityListeners;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Component
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Data
@Entity
@Table
public class Result {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
private int Id; 
private String Username;
private int Score;

public int getId() {
	return Id;
}
public void setId(int Id) {
	this.Id = Id;
}
public String getUsername() {
	return Username;
}
public void setusername(String username) {
	this.Username= username;
}
public int getScore(){
    return Score;
}
public void setScore(int Score){
    this.Score = Score;
}
@Override
public String toString() {
    return "Result [Id=" + Id + ", Username=" + Username + ", Score=" + Score + "]";
}


}
