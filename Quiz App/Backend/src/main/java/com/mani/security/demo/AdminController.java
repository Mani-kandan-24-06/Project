package com.mani.security.demo;

import io.swagger.v3.oas.annotations.Hidden;
import io.swagger.v3.oas.annotations.parameters.RequestBody;

import org.aspectj.weaver.patterns.TypePatternQuestions.Question;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin(origins="http:/localhost:3000") 
@RestController
@RequestMapping("/api/v1/admin")
@PreAuthorize("hasRole('ADMIN')")
public class AdminController {
    @Autowired
	Repository repository;
    @GetMapping
    @PreAuthorize("hasAuthority('admin:read')")
    public String get() {
        return "GET:: admin controller";
    }

    @PostMapping("question/create/")
    @PreAuthorize("hasAuthority('admin:create')")
     public Questions createQuestion(@RequestBody Questions createdQuestions) {
          return repository.save(createdQuestions);
    }
    
   
    
    @PutMapping("question/update/")
    @PreAuthorize("hasAuthority('admin:update')")
    public  Questions updateQuestion( @RequestBody Questions updatedQuestion) {
         return repository.save(updatedQuestion);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasAuthority('admin:delete')")
    public ResponseEntity<Void> deleteQuestion(@PathVariable Integer id) {
         repository.deleteById(id);
         return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }
}

